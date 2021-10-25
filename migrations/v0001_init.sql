create table capture (
    id uuid primary key not null,
    path character varying not null,
    captured_at timestamp with time zone,
    prediction_label character varying null,
    prediction_confidence numeric null,
    prediction_processing_time numeric null,
    status character varying not null default 'new'
);