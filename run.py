import argparse
from app import create_app

parser = argparse.ArgumentParser(description="纸片化学社区版数据后端服务器")
parser.add_argument("--develop", type=int, default=0, help="开启开发者模式")
args = parser.parse_args()

if args.develop:
    app = create_app(config_class="config.DevelopmentConfig")
else:
    app = create_app(config_class="config.Config")

if __name__ == "__main__":
    app.run()