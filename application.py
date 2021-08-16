from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os


class Application(Flask):
    def __init__(self, import_name):
        super(Application, self).__init__(import_name)
        self.config.from_pyfile('config/base_setting.py')

        # 使配置文件随环境变量ops_config的改变而改变
        if "ops_config" in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ["ops_config"])

        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__)
manager = Manager(app)