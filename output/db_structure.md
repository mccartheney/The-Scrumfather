**

**User Table**
| Field | Data Type | Primary Key |
|---|---|---|
| user_id | int | yes |
| name | varchar(50) | no |
| hair_color | varchar(50) | no |
| email | varchar(50) | no |

**Color Table**
| Field | Data Type | Primary Key |
|---|---|---|
| color_id | int | yes |
| name | varchar(50) | no |
| code | varchar(50) | no |

**Image Table**
| Field | Data Type | Primary Key |
|---|---|---|
| image_id | int | yes |
| url | varchar(255) | no |
| hair_color_id | int | foreign key (color_id) |

**Content Table**
| Field | Data Type | Primary Key |
|---|---|---|
| content_id | int | yes |
| title | varchar(50) | no |
| description | varchar(255) | no |
| hair_color_id | int | foreign key (hair_color_id) |

**Order Table**
| Field | Data Type | Primary Key |
|---|---|---|
| order_id | int | yes |
| user_id | int | foreign key (user_id) |
| color_id | int | foreign key (color_id) |
| order_date | datetime | no |
| order_status | varchar(50) | no |

**Analytics Table**
| Field | Data Type | Primary Key |
|---|---|---|
| analytics_id | int | yes |
| user_id | int | foreign key (user_id) |
| date | datetime | no |
| views | int | no |
| clicks | int | no |