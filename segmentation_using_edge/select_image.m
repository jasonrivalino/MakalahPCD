function filename = select_image()
    % Function to open a file explorer and select an image file
    % Output:
    %   filename - full path of the selected image file

    % File types filter for common image formats
    [file, path] = uigetfile({'*.jpg;*.jpeg;*.png;*.bmp;*.tiff', 'Image Files (*.jpg, *.jpeg, *.png, *.bmp, *.tiff)';
                               '*.*', 'All Files (*.*)'}, ...
                              'Select an Image File');
    
    % Check if the user canceled the selection
    if isequal(file, 0)
        error('No file was selected.');
    end
    
    % Construct the full file path
    filename = fullfile(path, file);
end