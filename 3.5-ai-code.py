# page fault is when a page that a program needs is not currently in the memory
from collections import deque

def fifo_page_replacement_genai():
    # Input: number of page frames
    while True:
        try:
            frame_count = int(input("Enter the number of page frames (3–6): "))
            if 3 <= frame_count <= 6:
                break
            else:
                print("Please enter a valid number between 3 and 6.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Input: reference string
    while True:
        reference_input = input("Enter the reference string (15–25 space-separated integers): ").strip()
        reference_string = reference_input.split()

        if all(i.isdigit() for i in reference_string) and 15 <= len(reference_string) <= 25:
            reference_string = list(map(int, reference_string))
            break
        else:
            print("Invalid reference string. Ensure it contains 15–25 integers.")

    # FIFO Page Replacement logic
    page_frames = deque()
    page_faults = 0

    for page in reference_string:
        if page not in page_frames:
            if len(page_frames) < frame_count:
                page_frames.append(page)
            else:
                page_frames.popleft()  # Remove oldest page
                page_frames.append(page)
            page_faults += 1

    print(f"\nTotal number of page faults: {page_faults}")

# Run the function
fifo_page_replacement_genai()
