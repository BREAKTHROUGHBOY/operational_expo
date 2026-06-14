from analysis import (
    calculate_total,
    categories_expenses,
    sort_categories,
    heighest_category,
    lowest_category,
    category_len,
    get_avg,
    transaction_dates,
    transaction_with_dates,
    get_monthly_expenses,
    generate_summary_report
)


def menu():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Total Expenses")
        print("2. Category Expenses")
        print("3. Sorted Categories")
        print("4. Highest Expense Category")
        print("5. Lowest Expense Category")
        print("6. Category Transaction Count")
        print("7. Average Expense")
        print("8. Transaction Dates")
        print("9. Transactions with Dates")
        print("10. Monthly Analysis")
        print("11. Summary Report")
        print("0. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            print(calculate_total())

        elif choice == "2":
            print(categories_expenses())

        elif choice == "3":
            print(sort_categories())

        elif choice == "4":
            print(heighest_category())

        elif choice == "5":
            print(lowest_category())

        elif choice == "6":
            print(category_len())

        elif choice == "7":
            print(get_avg())

        elif choice == "8":
            print(transaction_dates())

        elif choice == "9":
            print(transaction_with_dates())

        elif choice == "10":
            print(get_monthly_expenses())

        elif choice == "11":
            generate_summary_report()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()