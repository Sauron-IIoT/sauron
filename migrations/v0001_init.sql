create table capture (
    id uuid primary key not null,
    path character varying not null,
    captured_at timestamp with time zone
);