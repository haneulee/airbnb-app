# Airbnb API

REST & GraphQL API of the Airbnb Clone using Django REST Framework and Graphene GraphQL   
[restAPI good design](https://www.swipe.to/4287nc?p=Z4h7dGZHX)

### API Actions

- [ ] Login
- [ ] See Profile
- [ ] Create Account
- [ ] Edit Profile
- [ ] See Favs
- [X] List Rooms
- [X] See Room
- [ ] Filter Rooms
- [ ] Search By Coords
- [ ] Add Room to Favourites

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
