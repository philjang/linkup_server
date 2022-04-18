# Linkup
- Linkup is a full stack application that helps users stay better connected to their loved ones. This is my first project utilizing python/django. The purpose of this project was to learn more about the language and framework in use, and my hope was to gain some familiarity with how they function as a back-end technology - still a continuing work in progress.

## Project Description

As the world quickly got thrown into the chaos of COVID, many status quos were dynamically shifted. An absurd number of people across the globe saw negative impacts to too many parts of their lives, all at once. One of these facets was the dissolution of social connections, which has been a detriment to the mental well-being of a widespread population - an issue that is often deprioritized in lieu of more pressing or 'pragmatic' problems. Human beings are by nature communal creatures at our core and I want to leverage technology to address a basic need that society often deems simply extracurricular. I hope that this application will serve as a useful tool to help people gather together and engage one another to form progressively more genuine connections. 

## Link to Client Repository

[Code](https://github.com/philjang/linkup-client)

## Link to Current Version 

<!-- [Deployment Coming Soon...]() -->
Deployment Coming Soon...

## Product Screenshots (v1.0)
<details>
  <summary>Click to Display</summary>

- Landing Page
![Landing Page]()
- Register/Login Page
![Register/Login Page]()
- User Home Page
![User Home Page]()
- Group Page
![Group Page]()
- Discussion Page
![Discussion Page]()

</details>

## Installation Instructions -- Front-End

- Fork and clone code to desired directory
- `cd` into project directory
- Run `npm i` in your terminal to install dependencies:
    <details>
      <summary> List </summary>

      - axios
      - react-router-dom

    </details>
- Create a `.env.local` file in the root directory

    Inside `.env.local`:
    ```
    REACT_APP_SERVER_URL=http://127.0.0.1:<portNumber>
    ```
    Make sure that this port number matches what the server is running on, django default: 8000
- Run `npm start` in your terminal - client will run on port 3000 by default
    - Be sure to change the `CORS_ORIGIN_WHITELIST` inside the server settings.py accordingly if you wish to change this

## Installation Instructions -- Back End

- Form and clone code to desired directory, separate from the client directory
- `cd` into project directory
- Create and activate virtual environment with venv to install pip3 packages locally

    - Run `python -m venv <name_of_choice>` in your terminal
    - Then run `<name_of_choice>/bin/activate`

- Run `pip3 install -r requirements.txt` in your terminal to install dependencies:
    <details>
      <summary> List </summary>

      - axios
      - asgiref==3.5.0
      - dj-database-url==0.5.0
      - Django==4.0.4
      - django-cors-headers==3.11.0
      - django-rest-auth==0.9.5
      - djangorestframework==3.13.1
      - psycopg2==2.9.3
      - python-dotenv==0.20.0
      - pytz==2022.1
      - six==1.16.0
      - sqlparse==0.4.2

    </details>
- Create a `.env` file in the root directory

    Inside `.env`:
    ```
    ENV=development
    DB_NAME_DEV=<db_name>
    SECRET=<Django_SECRET_KEY>
    ```
- Inside your postgres shell, run `CREATE DATABASE <db_name>` - the two `<db_name>`s must match
- Run `python manage.py migrate` in your terminal
- Check database to confirm the migrations have been made to postgres
    - Can use posgres shell or a GUI like Postico
    - Can also use the python shell to create and test data if preferred - run `python manage.py shell`
- Run `python manage createsuperuser` and follow prompts to create an admin uesr
- Run `python manage.py runserver`
- In browser, go to `http://localhost:8000/admin` to access the django admin panel
- Once both the client and server are running, the app will be accessible in the browser - `https://localhost:3000` by default

## Technologies Used
- Python
- Django
- Django ORM
- Django Rest Framework
- Postgres
- React
- React Router Dom
- Javascript
- CSS
- Axios
- Heroku for Back-End Deployment
- Netlify for Front-End Deployment

## Development Approach

### User Stories
- As a user, I want to make a group and add my friends (mvp for admin to add any users, stretch for social-media style mutual add)
- As a user, I want a separate space to discuss specific topics, so that friends in the group will only have to see the content if they are interested
- As a user, I want to be able to create a post so that I can connect with my friends
- As a user, I want to be able to edit a post
- As a user, I want to be able to delete any posts that I created
- As a user, I want to be able to join multiple groups 
- As a user, I want to be able to see who is in my groups

### ERD
![ERD of database](assets/ERD.drawio.png)

### Wireframes
<details>
    <summary>Click to Display</summary>

![Landing Page](assets/Landing.png)
![Login/Register Page](assets/Login.png)
![User Home Page](assets/Profile.png)
![Group Page](assets/Group.png)
![Discussion Page](assets/Discussion.png)

</details>

## Front-End URL Patterns (React Routes)
| Path               | Purpose                                                 |
| ------------------ | ------------------------------------------------------- |
| `/`                | Landing Page                                            |
| `/login`           | Login Page                                              |
| `/register`        | Register Page                                           |
| `/profile`         | User home page that displays user's groups              |
| `/new`             | Page to create a new group                              |
| `/groups/:id`      | Group page that displays groups's discussions and users |
| `/discussions/:id` | Discussion page that displays discussions's posts       |

## RESTful Routing (Django Server API)
| Method | Path                        | Purpose                                                          |
| ------ | --------------------------- | ---------------------------------------------------------------- |
| POST   | `membership/register`       | CREATE a new user                                                |
| POST   | `membership/login`          | logs in an existing user, adds token to user and sends it back   |
| DELETE | `membership/logout`         | logs user out, removes token from user, deletes all session data |
| GET    | `membership/users/:id`      | READ all groups associated with current user                     |
| POST   | `membership/groups`         | CREATE a new group, makes current user admin                     |
| PUT    | `membership/groups/:id`     | UPDATE a group with :id, if admin                                |
| DELETE | `membership/groups/:id`     | DELETE a group with :id, if admin                                |
| GET    | `membership/groups/:id`     | READ all discussions and usernames associated to group with :id  |
| POST   | `membership/groups/:id/add` | CREATE a new M:N connection between group with :id and user      |
| DELETE | `membership/groups/:id/del` | DELETE the M:N connection between group with :id and user        |
| POST   | `api/discussions`           | CREATE a new discussion, makes current user admin                |
| PUT    | `api/discussions/:id`       | UPDATE a discussion with :id, if admin                           |
| DELETE | `api/discussions/:id`       | DELETE a discussion with :id, if admin                           |
| GET    | `api/discussions/:id`       | READ all posts associated to discussion with :id                 |
| POST   | `api/posts`                 | CREATE a new post, makes current user owner                      |
| PUT    | `api/posts/:id`             | UPDATE a post with :id, if owner                                 |
| DELETE | `api/posts/:id`             | DELETE a post with :id, if owner                                 |

## Future Goals
- Add ability to comment on specific posts
- Add sorting functionality for discussions
- Differentiate between public and private groups
- Add event making functionality (post-cohort stretch google calendar api)
- Polls for where to meet
- Add cloudinary photo posting
- Add youtube video embedding
- Add chatroom in groups (post-cohort stretch socket.io)
- Add video/voice in chat (post-cohort stretch agora)
- Sass for styling

<!-- ## Post-Project Reflection -->