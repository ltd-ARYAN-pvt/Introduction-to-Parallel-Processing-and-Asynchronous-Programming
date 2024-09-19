# Asynchronous Programming: Multithreading, Multi-core Processing, and Asyncio
*Author - Aryan Pandey*

Welcome to the **Asynchronous Programming** repository! This repo provides a hands-on guide to mastering parallel processing concepts and techniques such as **Multithreading**, **Multi-core Processing**, and **Asyncio** in Python. Whether you are a beginner or an intermediate learner, this repository offers basic programming files, along with project examples, to help you dive into asynchronous programming.

## Folder Structure

```
Asynchronous Programming/
│
├── 1) Multithreading/
│   ├── basics/
|   ├── project/
│   └── README.md
│
├── 2) Multi-core Processing/
│   ├── basics/
│   └── README.md
│
├── 3) Asyncio/
│   ├── basics/
│   ├── project/
│   └── README.md/
│
└── README.md
```

### Overview of Techniques

1. **Multithreading**  
   Learn how to run multiple threads concurrently, making your program more efficient when working with I/O-bound tasks (e.g., reading files, network calls).

2. **Multi-core Processing**  
   Take advantage of multiple CPU cores to distribute CPU-bound tasks, like heavy computations, across multiple processors.

3. **Asyncio**  
   Master event-driven programming using the `asyncio` library in Python to handle I/O-bound tasks asynchronously and improve the responsiveness of your application.

## Getting Started

1. **Clone the repository**
   ```
   git clone https://github.com/ltd-ARYAN-pvt/Introduction-to-Parallel-Processing-and-Asynchronous-Programming.git
   ```

2. **Set up the environment**  
   Make sure you have Python installed (version 3.7+ is recommended). You may want to set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

3. **Install dependencies**  
   Ayncio project example requires additional Python libraries. Navigate to the project folder and install required packages:
   ```
   pip install aiohttp
   ```

## Folder Details

### 1) Multithreading
- **Basics**:  
  Includes introductory examples to help you understand the concept of threads, creating and managing threads, synchronization, and thread-safe operations.

- **Projects**:  
  Image Downlaoder App:- Download apps parallely from `picsum.photos` using multithreading.

### 2) Multi-core Processing
- **Basics**:  
  Learn how to use Python’s `multiprocessing` library to run CPU-bound tasks on multiple cores.

- **Projects**:  
  For this i want you to try a `Random forest classifier model` and first set `n_jobs=-1` and see the training speed then set it to `default` and then see the speed of training.

### 3) Asyncio
- **Basics**:  
  Get started with asynchronous programming using Python’s `asyncio` library. Learn about async functions, coroutines, tasks, and the event loop.

- **Projects**:  
  Image Downlaoder App:- Download apps asynchronously from `picsum.photos` using `asyncio` and `aiohttp`.

## Example Usage

Here's a simple example of using **asyncio** to fetch data from multiple URLs:

```python
import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["https://example.com", "https://python.org"]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())
```

### Running a Project

To run a specific project, navigate to the respective folder, follow the instructions provided in the project’s `README.md`, and execute the Python scripts.

## Contribution Guidelines

Contributions are welcome! If you’d like to add more examples or projects:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Open a pull request.

Feel free to open issues if you encounter any problems or have questions!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
