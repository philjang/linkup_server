1. How do you plan on learning/implementing this new technology?
- Gitbook
- Django Tutorial/Documentation
- Online tutorials/articles/guides/stackoverflow
- Instructors' graceful assistance...

2. What is your goal with this project?
- To learn more about python and django in use and perhaps gain some familiarity
- To begin creating a functioning application that allows for many stretch goals that can be implemented post-cohort

3. Who is the user for your app?
- Anyone using the internet that wishes to engage with their friends more intentionally 

4. Any potential roadbloacks you think you might run into? 
- Learning a new, albeit widely used, technology does not instill much confidence over planning out the scope of the project
- I will try to start out with what I envision is a reasonable mvp, but this may still be biting off more than I can chew 
- With what I understand of python and django now, I'm not completely certain as to the scope of what I can learn and execute within a week's time, compared to what I might be able to do with familiar technologies (i.e. express and javascript)
- It will be interesting to see how similar tasks are accomplished by the framework and hopefully to see what else python/django has to offer

# Technologies Planned for Use
- Python
- Django
- Postgres
- React
- Axios

# Project Description

As the world quickly got thrown into the chaos of COVID, many status quos were dynamically shifted. An absurd number of people across the globe saw negative impacts to too many parts of their lives, all at once. One of these facets was the dissolution of social connections, which has been a detriment to the mental well-being of a widespread population, but an issue that is often deprioritized in lieu of more pressing or 'pragmatic' problems. Human beings are by nature communal creatures at our core and I want to leverage technology to address a basic need that society often deems simply extracurricular. I hope that this application will serve as a useful tool to help people gather together and engage one another to form progressively more genuine connections. 

# User Flow/User Stories
- As a user, I want to make a group and add my friends (mvp for admin to add any users, stretch for social-media style mutual add)
- As a user, I want a separate space to discuss specific topics, so that friends in the group will only have to see the content if they are interested
- As a user, I want to be able to create a post so that I can connect with my friends
- As a user, I want to be able to edit a post if I make a typo
- As a user, I want to be able to delete a post so that I can take back what I said
- As a user, I want to be able to join multiple groups 
- As a user, I want to be able to leave groups if needed

# Stretch Goals
- Add ability to comment on specific posts
- Differentiate between public and private groups
- Add event making functionality (post-cohort stretch google calendar api)
- Polls for where to meet
- Add cloudinary photo posting
- Add youtube video embedding
- Add chatroom in groups (post-cohort stretch socket.io)
- Add video/voice in chat (post-cohort stretch agora)
- Sass for styling

# Wireframes
- Will continue to work on this throughout the day and update, but I am prioritizing sleep for the sake of sustainability throughout the week. It took me longer than I thought to explore new technologies and decide on a project that I can be excited about without the mvp scope being too out there. Wireframes, ERDs, and RESTful routing will not likely be too different from previous projects in terms of complication for, as I am focusing on exploring python/django. Users M:N groups, groups 1:M discussions(topics), discussions 1:M posts, users 1:M posts.

# ERDs
![ERD of database](./ERD.drawio.png)

# URL Patterns
| Path               | Purpose                                                 |
| ------------------ | ------------------------------------------------------- |
| `/`                | Landing Page                                            |
| `/login`           | Login Page                                              |
| `/register`        | Register Page                                           |
| `/profile`         | User home page that displays user's groups              |
| `/groups/:id`      | Group page that displays groups's discussions and users |
| `/discussions/:id` | Discussion page that displays discussions's posts       |

# RESTful Routing
| Method | Path               | Purpose                                                      |
| ------ | ------------------ | ------------------------------------------------------------ |
| POST   | `/users`           | CREATE a new user                                            |
| GET    | `/users/:id`       | READ all groups associated with current user                 |
| POST   | `/groups`          | CREATE a new group                                           |
| PUT    | `/groups/:id`      | UPDATE a group with :id, if admin                            |
| DELETE | `/groups/:id`      | DELETE a group with :id, if admin                            |
| GET    | `/groups/:id`      | READ all discussions and users associated to group with :id  |
| POST   | `/discussions`     | CREATE a new discussion                                      |
| PUT    | `/discussions/:id` | UPDATE a discussion with :id, if admin                       |
| DELETE | `/discussions/:id` | DELETE a discussion with :id, if admin                       |
| GET    | `/discussions/:id` | READ all posts associated to discussion with :id             |
| POST   | `/posts`           | CREATE a new post                                            |
| PUT    | `/posts/:id`       | UPDATE a post with :id, if owner                             |
| DELETE | `/posts/:id`       | DELETE a post with :id, if owner                             |


# Sprints
- Tuesday: Review/Research Python/Django
- Wednesday: Begin back-end construction
- Thursday: Finish back-end and begin React front-end
- Friday: Finish front-end
- Saturday: Styling and refactoring