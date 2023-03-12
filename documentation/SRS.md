
# Rest Flask final application

# 1. Vision

"Rest_Flask" is web-application which allows manage information about users and attached to them posts.

The application should provide:
- Storing data about new users and posts in a database;
- Display list of users;
- Update list of users (add, edit, delete);
- Display list of posts;
- Update list of posts (add, edit, delete);
- Display list of posts for each user;
- Filtering for posts by date, user;

## 1.1. Users
### 1.1.1. Display list of users
*Main scenario:*

User selects "Users" menu tab, the application display list of users.

---
![Users_List](/documentation/mockups/listofusers.png)

---

**The page contains:**
#### 1) Menu with tabs
- Users
- Posts

#### 2) List of users
- Username
- First Name
- Last Name
- Location
- Posts
- Registered at

#### 3) Button for adding new user

**Possible actions:**
- click on "Posts" tab in menu to see full list of posts;
- click on user's name to jump to specitic userr page to see more details and edit or delete the user record;
- push "ADD" button to open user creating form.


### 1.1.2. Display the user
*Main scenario:*

User click on the user's name in the list of users the application jump to the user's detail view page.

---
![User](/documentation/mockups/userform.png)

---

**The page contains:**
#### 1) Menu with tabs
- Users
- Posts
#### 2) A table with the user's information
- Photo
- Username
- First name
- Last name
- Location
- Posts
- Registered at

#### 3) Buttons
- EDIT the users info
- DELETE the user

#### 4) List of posts curently supervised by the user
- Title
- Description
- Likes

#### 5) Button to add a post

**Possible actions:**
- click on  user" or "posts" tab in menu to see full list of users or posts respectively;
- push "EDIT" button to change information about the user;
- push "DELETE" button to delete the user;
- click on post's name to jump to specitic post page to see more details and edit or delete the post record;
- push "ADD" button to create a post linked to this user

### 1.1.3. ADD or EDIT the user
*Main scenario:*

User either push "ADD" button on the page with list of users
or "EDIT" button on the particular user's page, the application jump to the user creation/edit form.

---
![user_edit](/documentation/mockups/addedituser.png)

---

**The page contains:**
#### 1) Menu with tabs
- users
- posts
#### 2) A table for the user's information. Table fields either contains actual information in case of editing, or are empty in case of creating new user
- Photo
- Username
- First name
- Last name
- Location
- Posts

#### 3) Buttons
- SAVE

**Possible actions:**
- click on  user" or "posts" tab in menu to see full list of users or posts respectively;
- edit fields for input;
- push "SAVE" button to save the user's info;


## 1.2. Posts
### 1.2.1. Display list of posts
*Main scenario:*

As User select "posts" menu tab, the application display list of posts.

---
![post_List](/documentation/mockups/listofposts.png)

---

**The page contains:**
#### 1) Menu with tabs
- users 
- posts
#### 2) Search block with next elements
- "User" filter drop-down list field
- "SEARCH" Button
#### 3) List of posts
- Title
- Description
- Likes
- Author
- Created at

**Possible actions:**
- click on  users" tab in menu to see full list of users;
- fill search form fields and click "SEARCH" button to change list of posts according to search criterias;
- click on post's name to jump to specitic post page to see more details and edit or delete the post's record;
- click on user's name to jump to specitic user page to see more details and edit or delete the user record.


### 1.2.2. Display the post
*Main scenario:*

User click on the posts's name in the list of posts the application jump to the posts's detail view page.

---
![post](/documentation/mockups/postform.png)

---

**The page contains:**
#### 1) Menu with tabs
- Users
- Posts
#### 2) A table with the post's information
- Title
- Description
- Likes
- Author
- Created at

#### 3) Buttons
- EDIT the posts info
- DELETE the post

**Possible actions:**
- click on  user" or "posts" tab in menu to see full list of users or posts respectively;
- push "EDIT" button to change information about the post;
- push "DELETE" button to delete the post;
- click on users's name to jump to specitic user page to see more details and edit or delete the user record;


### 1.2.3. ADD or EDIT the post
*Main scenario:*

User either push "ADD" button on the user's page with list of post
or "EDIT" button on the particular posts's page, the application jump to the post creation/edit page.

---
![Post_Edit](/documentation/mockups/addeditpost.png)

---

**The page contains:**
#### 1) Menu with tabs
- users
- posts
#### 2) A table for the post's information. Table fields either contains actual information in case of editing, or are empty in case of creating new post
- Title
- Description
- Author
- Created at

#### 3) Buttons
- SAVE

**Possible actions:**
- click on  user" or "posts" tab in menu to see full list of users or posts respectively;
- edit fields for imput;
- push "SAVE" button to save the posts's info.

=======================================================================
