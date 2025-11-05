
import os

bad = "c1a4be04b972b6c17db242fc37752ad517c29402"
good = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

test_cmd = "python manage.py test -q"

os.system(f"git bisect start {bad} {good}")
os.system(f"git bisect run {test_cmd}")
os.system("git bisect reset")
