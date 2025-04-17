**

**Database Schema:**

**Users Table:**
- user_id (INT, PRIMARY KEY AUTO_INCREMENT)
- username (VARCHAR(50) UNIQUE)
- email (VARCHAR(255) UNIQUE)
- password (VARCHAR(255))

**Posts Table:**
- post_id (INT, PRIMARY KEY AUTO_INCREMENT)
- user_id (INT, FOREIGN KEY REFERENCES Users(user_id))
- title (VARCHAR(50))
- content (TEXT)
- image (VARCHAR(255))
- visibility (ENUM('public', 'private', 'friends'))
- location (VARCHAR(255))
- created_at (DATETIME)

**Likes Table:**
- like_id (INT, PRIMARY KEY AUTO_INCREMENT)
- user_id (INT, FOREIGN KEY REFERENCES Users(user_id))
- post_id (INT, FOREIGN KEY REFERENCES Posts(post_id))

**Comments Table:**
- comment_id (INT, PRIMARY KEY AUTO_INCREMENT)
- user_id (INT, FOREIGN KEY REFERENCES Users(user_id))
- post_id (INT, FOREIGN KEY REFERENCES Posts(post_id))
- content (TEXT)

**Tags Table:**
- tag_id (INT, PRIMARY KEY AUTO_INCREMENT)
- tag_name (VARCHAR(50))

**Categories Table:**
- category_id (INT, PRIMARY KEY AUTO_INCREMENT)
- category_name (VARCHAR(50))

**Relationships:**

- A User can have many Posts.
- A Post can have many Likes and Comments.
- A Post can have many Tags and Categories.

**Indexes:**

- Users table: username, email
- Posts table: post_id, user_id, title, content, image, visibility
- Likes table: user_id, post_id
- Comments table: user_id, post_id
- Tags table: tag_id, tag_name
- Categories table: category_id, category_name

**Additional Features:**

- File Manager: store and access user images.
- Comment System: store and manage comments.
- Notifications: send alerts for new comments and reactions.
- Social Media Integration: allow users to sign in with existing social media credentials.