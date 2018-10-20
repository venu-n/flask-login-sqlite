from app import create_app, db
from app.auth.models import User

if __name__ == '__main__':
    flask_app = create_app('dev')
    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name='venu').first():
            User.create_user(user='venu',
                             email='venu@venu.com',
                             password='email')
    flask_app.run()