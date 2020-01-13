# Airbnb API

REST & GraphQL API of the Airbnb Clone using Django REST Framework and Graphene GraphQL

### API Actions

- [ ] List Rooms
- [ ] Filter Rooms
- [ ] Search By Coords
- [ ] Login
- [ ] Create Account
- [ ] See Room
- [ ] Add Room to Favourites
- [ ] See Favs
- [ ] See Profile
- [ ] Edit Profile

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