from TaskTrackerModule import TaskTracker

# Main function
def main():
    tracker = TaskTracker()
    # tracker.clear_screen()
    while True:
        tracker.clear_screen()
        tracker.display_menu()
        choice = tracker.get_choice()

        match choice:
            case '1':
                tracker.add_task()
            case '2':
                tracker.view_tasks()
                tracker.back_to_menu()
            case '3':
                tracker.mark_task_completed()
            case '4':
                tracker.delete_task()
            case '5':
                tracker.save_tasks_to_file()
            case '6':
                tasks = tracker.load_tasks_from_file()
            case '7':
                print("\n\nGoodbye!\n\n")
                break
            case _:
                print("Invalid choice. Please try again.")
    

if __name__ == "__main__":
    main()