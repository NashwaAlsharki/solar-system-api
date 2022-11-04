from flask import Blueprint, jsonify
from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    mass = db.Column(db.String)
    moon_id = db.Column(db.Integer, db.ForeignKey('moon.id'))
    moons = db.relationship("Moon", back_populates="planet")
