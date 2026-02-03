# Sorting Algorithms Visualization Platform
### DAA Project - Semester 5

This project is a full-stack web application designed to visualize various sorting algorithms. It helps in understanding the mechanics of sorting algorithms, their time complexity, and performance through step-by-step visualization.

## 🚀 Tech Stack

### Backend
- **Language**: Python 3
- **Framework**: Django & Django REST Framework (DRF)
- **Features**: 
  - Implementation of sorting algorithms (Bubble, Selection, Insertion, Merge, Quick, Heap) from scratch.
  - Step-by-step state tracking.
  - Performance metrics (Comparisons, Swaps, Execution Time).

### Frontend
- **Library**: React.js (Vite)
- **Styling**: Tailwind CSS
- **Features**:
  - Interactive visualization of array sorting.
  - Controls for algorithm selection, array size, and speed.
  - Real-time metrics display.

## 📂 Project Structure

```
d:/Project/SEM_5/DAA/
├── backend/                 # Django Backend
│   ├── apps/sorting/        # Sorting Application
│   │   ├── algorithms/      # Algorithm implementations
│   │   ├── api/             # API Views and Serializers
│   │   └── services/        # Helper services (StepTracker)
│   ├── sorting_visualizer/  # Project Configuration
│   └── manage.py
│
├── frontend/                # React Frontend
│   ├── src/
│   │   ├── components/      # UI Components (Controls, Charts)
│   │   ├── pages/           # Main Views
│   │   └── services/        # API integration
│   ├── tailwind.config.js
│   └── vite.config.js
│
└── README.md
```

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.x
- Node.js & npm

### Backend Setup
1. Navigate to the backend directory:
   ```powershell
   cd backend
   ```
2. Create and activate virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```powershell
   python manage.py migrate
   ```
5. Start the server:
   ```powershell
   python manage.py runserver
   ```
   The API will be available at `http://localhost:8000/`.

### Frontend Setup
1. Navigate to the frontend directory:
   ```powershell
   cd frontend
   ```
2. Install dependencies:
   ```powershell
   npm install
   ```
3. Start the development server:
   ```powershell
   npm run dev
   ```
   The application will be accessible at `http://localhost:5173/`.

## 🎓 Educational Notes

- **Algorithms**: All sorting algorithms are implemented in `backend/apps/sorting/algorithms/`.
- **Step Tracking**: `StepTracker` class in `backend/apps/sorting/services/step_tracker.py` is used to capture the state of the array after every significant operation (compare/swap).
- **Visualization**: The frontend receives a list of steps from the backend and animates them using `setTimeout`.

## 🧪 Algorithms Implemented
1. **Bubble Sort**: `O(n^2)`
2. **Selection Sort**: `O(n^2)`
3. **Insertion Sort**: `O(n^2)`
4. **Merge Sort**: `O(n log n)`
5. **Quick Sort**: `O(n log n)`
6. **Heap Sort**: `O(n log n)`

## 📸 Screenshots
*(Add screenshots here after running the project)*
