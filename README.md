# Full-Stack Developer Challenge

Welcome to the Full-Stack Developer Challenge! In this task, you will create a simple full-stack application using FastAPI for the backend and React for the frontend. The application will visualize data in a chart and allow users to download the data as a CSV file.

---

## Task Description

### **Objective**
Build a full-stack application that includes:
1. A FastAPI backend to manage data points.
2. A React frontend to visualize the data and enable user interactions.

---

### **Requirements**

#### **Backend (FastAPI)**

1. **API Endpoints:**
   - `GET /data`: Returns a list of data points in the format:
     ```json
     [
       {"x": 1, "y": 10},
       {"x": 2, "y": 20},
       {"x": 3, "y": 30}
     ]
     ```
   - `POST /data`: Accepts a JSON object with `x` and `y` values to add a new data point to the list.
     ```json
     {
       "x": 4,
       "y": 40
     }
     ```

2. **Storage:**
   - Data can be stored in memory (no database setup required).

---

#### **Frontend (React)**

1. **Data Visualization:**
   - Display the data points fetched from the `/data` API in a chart (e.g., a line chart or scatter plot).
   - Use a charting library like **Chart.js** or **Recharts**.

#### **Bonus Questions**

2. **Add New Data:**
   - Provide a form with inputs for `x` and `y` values and a submit button.
   - Submit the form to add the new data point via the `/data` API.
   - Update the chart dynamically after adding the new data point.

3. **Export to CSV:**
   - Include a button to generate a CSV file of the data points in `(x, y)` format.
   - Allow users to download the CSV file.

4. **Additional Features:**
   - Use Axios or Fetch API for making API calls.
   - Handle errors gracefully (e.g., display an error message if an API call fails).
   - Style the application minimally for clarity and usability.
