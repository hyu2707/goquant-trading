import os
import yaml
from os.path import expanduser

from entity.constants import ENV_TEST_LEVEL, TEST_LEVEL_INTEGRATION


class TradingConfig(object):
    def __init__(self, config=None):
        if config is None:
            config = os.environ.get('RUNTIME_ENV', 'development')
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self._load_config(config)

    def _load_config(self, env="development"):
        # load config
        yaml_file = "{}/{}.yaml".format(self.dir_path, env)
        priv_yaml_file = "{}/priv.yaml".format(self.dir_path)

        print("load config: {}".format(yaml_file))
        with open(yaml_file, 'r') as f:
            self.config = yaml.safe_load(f)

        self.logging_level = self.config["dev"]["logging_level"]
        self.logging_file = self.config["dev"]["logging_file"]
        self.ib_ip = self.config["ib"]["ip"]
        self.ib_port = self.config["ib"]["port"]
        self.ib_clientId = self.config["ib"]["clientId"]

        assert self.logging_level
        assert self.logging_file
        assert self.ib_ip
        assert self.ib_port

        self.alpaca_url = self.config["alpaca"]["url"]
        assert self.alpaca_url

        # data
        base_folder = self.config["data"]["base_folder"]
        csv_folder_name = self.config["data"]["csv_folder"]
        self.base_folder = "{}/{}".format(expanduser("~"), base_folder)
        self.csv_data_path = "{}/{}".format(self.base_folder, csv_folder_name)
        if not os.path.exists(self.csv_data_path):
            os.makedirs(self.csv_data_path)

        assert self.csv_data_path

        self.logging_file = "{}/{}".format(self.base_folder, self.logging_file)

        self.bitmex_orderbook_freq = self.config["data"]["bitmex_orderbook"]["freq"]
        self.bitmex_orderbook_symbols = self.config["data"]["bitmex_orderbook"]["symbols"]
        self.bitmex_orderbook_s3 = self.config["data"]["bitmex_orderbook"]["s3"]
        self.ws_sleep_time = self.config["data"]["ws_sleep_time"]

        if self.bitmex_orderbook_freq < self.ws_sleep_time:
            raise ValueError("bitmex_orderbook_freq must larger than ws_sleep_time")

        # kafka
        self.kafka_topic_bitmex_orderbook = self.config["kafka"]["topic_bitmex_orderbook"]
        self.kafka_bootstrap_servers = self.config["kafka"]["bootstrap_servers"]

        assert self.kafka_topic_bitmex_orderbook
        assert self.kafka_bootstrap_servers

        # private data
        if os.getenv(ENV_TEST_LEVEL) == TEST_LEVEL_INTEGRATION or env != "test":
            print("load priv config: {}".format(yaml_file))
            with open(priv_yaml_file, 'r') as f:
                self.priv_config = yaml.safe_load(f)

            self.alpaca_id = self.priv_config["alpaca"]["id"]
            self.alpaca_key = self.priv_config["alpaca"]["key"]
            self.polygon_key = self.priv_config["polygon"]["key"]
            self.binance_api_key = self.priv_config["binance"]["key"]
            self.binance_secret_key = self.priv_config["binance"]["secret"]
            # self.aws_id = self.priv_config["aws"]["id"]
            # self.aws_key = self.priv_config["aws"]["key"]
            # self.bitmex_id = self.priv_config["bitmex"]["id"]
            # self.bitmex_key = self.priv_config["bitmex"]["key"]

            # self.airflow_email = self.priv_config["service"]["airflow"]["email"]
        else:
            self.alpaca_id = self.config["alpaca"]["id"]
            self.alpaca_key = self.config["alpaca"]["key"]
            self.polygon_key = self.config["polygon"]["key"]
            self.binance_api_key = self.config["binance"]["key"]
            self.binance_secret_key = self.config["binance"]["secret"]

            # self.aws_id = self.config["aws"]["id"]
            # self.aws_key = self.config["aws"]["key"]
            # self.bitmex_id = self.config["bitmex"]["id"]
            # self.bitmex_key = self.config["bitmex"]["key"]

            # self.airflow_email = self.config["service"]["airflow"]["email"]

        assert self.alpaca_id  # it's in priv.yaml
        assert self.alpaca_key  # it's in priv.yaml
