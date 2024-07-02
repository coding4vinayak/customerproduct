
CREATE TABLE form (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP,
    status BOOLEAN DEFAULT FALSE,
    user_id INT

);

insert into form (name, email, phone, message, user_id) values ('John Doe', 'asda@gmail.com',458745512,'hi ok', 334)