from app import create_app, db
# from flask_script import Manager, Shell, Server

# from flask_migrate import Migrate, MigrateCommand

app = create_app('default')
# manager = Manager(app)


# migrate = Migrate(app, db)


# def make_shell_context():
#     return dict(app=app, db=db)


# manager.add_command("runserver", Server(host="127.0.0.1", port=5000, use_debugger=True))
# manager.add_command('shell', Shell(make_context=make_shell_context))
# # manager.add_command('db', MigrateCommand)
#
#
# if __name__ == '__main__':
#     manager.run()
# if __name__ == "__main__":
#     from werkzeug.serving import run_simple
#     run_simple("0.0.0.0", 5000, application=app, use_reloader=False, use_debugger=True, threaded=True)


