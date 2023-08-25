from example_app import views

routes = [
    ("POST", "/api/entity", views.entity.create),
    ("PUT", "/api/entity", views.entity.update),
    ("DELETE", "/api/entity", views.entity.delete),
    ("GET", "/api/entity/<int:entity_id>", views.entity.read),
    ("GET", "/api/entity", views.entity.read_all),
    ("GET", "/api/entity/error", views.entity.raise_error),
]
