% Pilih dan load program
filename = select_image();
img = read_image(filename);

% Deteksi tepi pada citra
image_edge_detection = canny_edge_detection(img);

% Melakukan segmentasi objek berdasarkan hasil deteksi tepi
image_segmentation_result = segmentation_using_edge(img, image_edge_detection, 2, 400);

% Menampilkan hasil sebelum dan sesudah deteksi tepi
figure;
subplot(1, 3, 1);
imshow(img);
title("Gambar Asli");

subplot(1, 3, 2);
imshow(image_edge_detection);
title("Gambar Hasil Deteksi Tepi");

subplot(1, 3, 3);
imshow(image_segmentation_result);
title("Gambar Hasil Segmentasi Objek");