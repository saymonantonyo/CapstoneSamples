import cv2
import numpy as np

# Load your image
image = cv2.imread("Hatchback_A-23-_png_jpg.rf.a6938721da6ea46bfcbd58f61177375a.jpg")  # Replace with your image path

# Define category names and their corresponding coordinates
categories = {
    "A1": [(243.186, 253.584), (280.754, 273.710), (220.377, 339.454), (185.492, 313.962)],
    "A2": [(304.905, 243.522), (341.802, 261.635), (298.197, 326.037), (256.603, 299.203)],
    "A3": [(402.851, 248.888), (368.637, 309.937), (324.360, 283.773), (359.916, 229.433)],
    "A4": [(416.939, 222.054), (460.545, 240.167), (434.381, 295.849), (388.092, 273.710)],
    "A5": [(470.607, 216.016), (507.505, 233.459), (492.746, 283.773), (450.482, 262.976)],
    "A6": [(545.744, 229.433), (539.706, 271.698), (500.796, 253.584), (511.530, 214.675)],
    "A7": [(547.085, 211.320), (544.402, 246.205), (578.616, 264.318), (577.945, 226.079)],
    "B7": [(611.488, 285.786), (612.830, 364.276), (577.274, 341.467), (579.958, 271.027)],
    "B6": [(541.719, 278.406), (532.327, 354.884), (575.932, 382.389), (577.945, 297.861)],
    "B5": [(526.289, 409.224), (471.949, 376.352), (494.758, 285.786), (537.023, 307.924)],
    "B4": [(435.052, 302.557), (392.788, 395.807), (455.178, 441.425), (483.354, 327.379)],
    "B3": [(369.979, 316.645), (318.322, 418.616), (375.345, 454.171), (415.597, 343.480)],
    "B2": [(290.817, 475.639), (239.832, 437.400), (297.526, 331.404), (344.486, 362.264)],
    "B1": [(206.960, 493.081), (269.350, 383.060), (221.048, 344.150), (149.937, 438.071)],
}

# Define colors for visualization
colors = {
    "A": (0, 255, 0),  # Green
    "B": (255, 0, 0),  # Blue
}

# Draw polylines on the image
for category, points in categories.items():
    pts = np.array(points, np.int32).reshape((-1, 1, 2))  # Convert to proper shape
    color = colors["A"] if category.startswith("A") else colors["B"]  # Select color
    cv2.polylines(image, [pts], isClosed=True, color=color, thickness=2)
    
    # Calculate the centroid of the rectangle
    centroid_x = int(sum(p[0] for p in points) / len(points))
    centroid_y = int(sum(p[1] for p in points) / len(points))
    
    # Draw a small circle at the centroid
    cv2.circle(image, (centroid_x, centroid_y), radius=5, color=(0, 0, 255), thickness=-1)  # Red color for the centroid
    
    # Put the category text at the centroid
    cv2.putText(image, category, (centroid_x, centroid_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Show the image
cv2.imshow("Polylines on Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()