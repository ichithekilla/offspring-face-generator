# Offspring Face Generator

A beginner-friendly AI demo web app: randomly selects a "father" and "mother" face (from AI-generated images), and blends their features to create a synthetic "offspring" face by pixelwise image averaging.

## Features

- Randomly picks two parents (male/female) from provided image folders
- Generates an "offspring" face by blending both parents
- Built with Streamlit for an easy web UI

## How to Run

1. **Install requirements**  
   ```
   pip install -r requirements.txt
   ```
2. **Add Your Images**  
   - Place at least 1 image in each: `faces/male/`, `faces/female/`  
   - Use `.jpg` or `.png` files (AI-generated faces recommended)
3. **Start the app**  
   ```
   streamlit run app.py
   ```

## Notes

- This project is for educational, non-commercial use
- No real faces are included in this repo.
- You can easily extend it by improving the blending logic, UI, or enabling user uploads.

## Example

![App Example Screenshot](screenshot.png)

---