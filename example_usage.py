"""Example usage for Sutherland-Hodgman Polygon Clipping Skill."""
from client import SutherlandHodgman

def main():
    print("Executing Sutherland-Hodgman Polygon Clipping...")
    subj = [(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0)]
    clip_box = [(1.0, 1.0), (3.0, 1.0), (3.0, 3.0), (1.0, 3.0)]
    clipped = SutherlandHodgman.clip(subj, clip_box)
    print("Clipped polygon:", clipped)
    assert len(clipped) == 4, f"Expected 4 vertices, got {len(clipped)}"
    print("Sutherland-Hodgman verified successfully!")

if __name__ == "__main__":
    main()
