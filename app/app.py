# Feature: User Login Module
# Student Management System - Main Application
# Base + Login module merged
from flask import Flask, jsonify
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "studentdb")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASS = os.getenv("DB_PASS", "admin123")

def get_db():
    return psycopg2.connect(
        host=DB_HOST, database=DB_NAME,
        user=DB_USER, password=DB_PASS,
        cursor_factory=RealDictCursor
    )

@app.route("/")
def home():
    return jsonify({"message": "Student Management System API"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/api/students", methods=["GET"])
def get_students():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
