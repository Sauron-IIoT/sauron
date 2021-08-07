from app.repository.capture import fetch_one, save_local

capture = fetch_one()
save_local(capture)