from .db import db, environment, SCHEMA, add_prefix_for_prod

class Review(db.Model):
    __tablename__ = "reviews"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    post_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("posts.id")))
    comment = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.TIMESTAMP)

    # relations
    reviewer = db.relationship("User", back_populates="user_reviews")
    post = db.relationship("Post", back_populates="reviews")

    def to_dict(self):
        return {
            "id": self.id,
            "comment": self.comment,
            "post_id": self.post_id,
            "created_at": self.created_at.isoformat().split('T')[0] if self.created_at else None,
        }
