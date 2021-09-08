create table capture (
    id uuid primary key not null,
    path character varying not null,
    captured_at timestamp with time zone,
    classification_score numeric null,
    is_uploaded boolean not null default false
);