"""Detect a green-ish region from a webcam using OpenCV."""

import argparse


def main():
    try:
        import cv2
        import numpy as np
    except ImportError:
        raise SystemExit(
            "Missing dependencies. Run: pip install -r requirements-vision.txt"
        )

    parser = argparse.ArgumentParser()
    parser.add_argument("--camera", type=int, default=0)
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        raise SystemExit(f"Cannot open camera {args.camera}; try --camera 1.")

    lower = np.array([35, 60, 50], dtype=np.uint8)
    upper = np.array([85, 255, 255], dtype=np.uint8)

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print("Failed to read frame.")
                break

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower, upper)
            contours, _ = cv2.findContours(
                mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )

            if contours:
                contour = max(contours, key=cv2.contourArea)
                if cv2.contourArea(contour) > 100:
                    moments = cv2.moments(contour)
                    if moments["m00"] > 0:
                        cx = int(moments["m10"] / moments["m00"])
                        cy = int(moments["m01"] / moments["m00"])
                        cv2.circle(frame, (cx, cy), 6, (0, 0, 255), -1)
                        cv2.putText(
                            frame, f"pixel=({cx}, {cy})", (cx + 8, cy),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1
                        )

            cv2.imshow("Color detection - press q to quit", frame)
            cv2.imshow("Mask", mask)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
