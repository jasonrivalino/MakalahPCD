import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# File dialog untuk memilih gambar
def choose_image():
    Tk().withdraw()  # Hide the main tkinter window
    file_path = askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    return file_path

# Pemilihan gambar
image_path = choose_image()
if not image_path:
    print("No image selected!")
    exit()

# Load dan konversi gambar ke RGB
img = cv2.imread(image_path)
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Reshape gambar ke format 2D array dan konversi ke float32
pixel_vals = image.reshape((-1, 3))
pixel_vals = np.float32(pixel_vals)

# Menentukan kriteria konvergensi dan jumlah cluster
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

# Jumlah cluster yang diinginkan
k = 5
_, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Konversi nilai centroid ke tipe data integer
centers = np.uint8(centers)
segmented_data = centers[labels.flatten()]
segmented_image = segmented_data.reshape(image.shape)

# Hitung ukuran rata-rata cluster
threshold_size = np.mean([np.sum(labels == i) for i in range(k)])

# Filter cluster berdasarkan ukuran
filtered_image = np.zeros_like(image)

for i in range(k):
    # Membuat mask untuk setiap cluster
    mask = (labels.flatten() == i).reshape(image.shape[:2])
    
    # Menghitung ukuran cluster
    cluster_size = np.sum(mask)
    
    if cluster_size <= threshold_size:
        # Assign cluster untuk cluster yang lebih kecil dari threshold
        filtered_image[mask] = centers[i]

    # Visualisasi cluster
    cluster_image = np.zeros_like(image)
    cluster_image[mask] = centers[i]

# Buat mask dari filtered image
mask = np.any(filtered_image > 0, axis=-1).astype(np.uint8)

# Implementasi mask ke gambar asli
result_image = img * mask[..., np.newaxis]

# Konversi hasil ke format RGB
result_image_rgb = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)

# Menampilkan hasil
plt.figure(figsize=(12, 12))

plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(segmented_image)
plt.title(f"Segmented Image with {k} Clusters")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(filtered_image)
plt.title(f"Filtered Image with Clusters ≤ {threshold_size} Pixels")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(result_image_rgb)
plt.title("Final Image with Applied Mask")
plt.axis("off")

plt.tight_layout()
plt.show()