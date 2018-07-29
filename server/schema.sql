CREATE TABLE IF NOT EXISTS messages (
    id bigint PRIMARY KEY,
    message text not null
    CHECK (char_length(message) <= 2000)
)
;
