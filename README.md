# Airbnb API

REST & GraphQL API of the Airbnb Clone using Django REST Framework and Graphene GraphQL   
[restAPI good design](https://www.swipe.to/4287nc?p=Z4h7dGZHX)

### API Actions

- [ ] Login
- [ ] Create Account
- [ ] See Profile
- [ ] Edit Profile
- [ ] Add/Room Room From Favourites
- [X] List Rooms
- [X] See Room
- [ ] Create Room
- [X] Edit Room
- [ ] Delete Room
- [ ] Search Rooms

### initial

git clone [remote git address] --branch [branch name] --single-branch [folder name]
git remote -v
rm -rf .git
git init
git remote add origin [remote git address]
pipenv shell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py mega_seed

### API
pipenv install djangorestframework

### admin
python manage.py createsuperuser

