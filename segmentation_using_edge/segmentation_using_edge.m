function image_segmentation_result = segmentation_using_edge(img, image_edge_detection, radius, min_pixel_area)
    % Binerisasi citra hasil deteksi tepi
    binarize_result = imbinarize(image_edge_detection, graythresh(image_edge_detection));

    % Operasi closing pixel
    cleaned_edges = imclose(binarize_result, strel('disk', radius));
        
    % Operasi untuk menghilangkan border
    cleaned_edges = imclearborder(cleaned_edges);

    % Operasi untuk mengisi lubang
    cleaned_edges = imfill(cleaned_edges, 'holes');

    % Operasi opening pixel
    cleaned_edges = imopen(cleaned_edges, strel('disk', radius));

    % Operasi untuk menghilangkan region kecil
    cleaned_edges = bwareaopen(cleaned_edges, min_pixel_area);

    % Hasil akhir segmentasi objek
    largest_region_mask = cleaned_edges;

    % Membuat mask
    mask = uint8(largest_region_mask);

    % Mengalikan mask dengan citra asli
    image_segmentation_result = img .* mask;
end