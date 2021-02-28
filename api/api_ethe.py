import etherscan
from sql_api import SQLite
from decimal import Decimal
from convers import dec_to_base, convert_base


class WorkApiEtherscan():


    def __init__(self):
        self.bd = SQLite()
        self.api_key = "api_key"
        self.es = etherscan.Client(
                    api_key= self.api_key,
                    cache_expire_after=5,
                    )


    #insert information in sql
    def etherscan_api(self):
        # GET LAST BLOCK
        blockNumber = self.es.get_block_number()
        # last 100 block
        for block_number in range(blockNumber, blockNumber-100, -1):
            block = self.es.get_block_by_number(block_number = block_number)
            # Conversion in 10 to 16
            getBlockByNumbe = dec_to_base(int(block_number), 16)
            tag = f"0x{getBlockByNumbe}".lower()
            # iter from tranzaction
            for from_rartzaktion in block['transactions']:
                x = convert_base(from_rartzaktion['value'])
                # divide value becose Ether wei 10**18
                eth_value = Decimal(x)/Decimal(1000000000000000000)
                # inser in to sql
                self.bd.insert_info_tranzaction(int(eth_value), from_rartzaktion['from'], from_rartzaktion['to'], tag)


    # select get_greatest_value in sql
    def get_greatest_value(self):
        great = sorted(self.bd.select_total_count_value())[-1][1]
        url = f"https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag={great}&boolean=true"
        return url


    # delete bd
    def delet_info(self):
        self.bd.delet_info()


api_etherscan = WorkApiEtherscan()
#api_etherscan.etherscan_api() 
#api_etherscan.bd.delet_info()
#api_etherscan.get_greatest_value()

