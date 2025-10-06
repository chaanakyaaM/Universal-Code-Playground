# 🧑‍💻 Contributing to Universal-Code-Playground | Hacktoberfest 2025
**Welcome! 👋** We're building the largest library of code fundamentals, and every contribution, no matter how small, helps define this massive project. By keeping your submission focused and correctly placed, we can ensure a near-instant merge!

🤝 Prerequisites & Agreements
By contributing to this repository, you agree to the following:

* Contributor License Agreement (CLA): You agree to the terms defined in the [LICENSE](https://github.com/IamBisrutPyne/Universal-Code-Playground/blob/main/LICENSE) of this repository.

* Code of Conduct (CoC): You agree to respect the [Code of Conduct](https://github.com/IamBisrutPyne/Universal-Code-Playground/docs/blob/main/COC).

## ☕ In a Nutshell: Contribution Flow
1. **Find a Missing Snippet:** Check our **Open Issues** or browse the folders for a language/concept that needs implementation.

2. **Code & Place:** Implement the code and place it in the correct folder (see structure below).

3. **Commit & PR:** Commit your changes using a descriptive message and open a Pull Request (PR).

* Crucial for Hacktoberfest: Submit one new program per PR. A PR must be merged or labeled with hacktoberfest-accepted by a maintainer to count.

## 📂 Repository Structure & Naming
To maintain navigation and consistency, please adhere to these structure and naming rules.

### 1. Folder Placement
All code is nested under the `Snippets/` folder, organized first by **Concept**, then by **Language**.

| Folder | What Belongs Here | Example Contribution Path |
| :--- | :--- | :--- |
| **`Basics`** | "Hello World," user input, basic loops, simple functions. | `snippets/Basics/Python/hello_world.py` |
| **`Algorithms`** | Sorting, Searching, Mathematical functions (Factorial, Fibonacci). | `snippets/Algorithms/Java/binary_search.java` |
| **`OOP`** | Classes, Inheritance, Polymorphism, and Encapsulation demos. | `snippets/OOP/Java/VehicleInheritance.java` |
| **`DataStructures`** | Simple implementations of lists, stacks, queues, trees, and maps. | `snippets/DataStructures/C/singly_linked_list.c` |
| **`DesignPatterns`** | Factory, Singleton, Observer, Strategy patterns. | `snippets/DesignPatterns/Go/factory_method.go` |
| **`Utilities`** | OS interactions, file I/O, simple regex demos. | `snippets/Utilities/Rust/read_file_sync.rs` |

### 2. File Naming Convention
Use the standard naming convention for the language you are contributing to (e.g., `snake_case` for Python, `PascalCase` for Java/C#).

* **Primary Rule:** The file name must be **descriptive** of the concept.

* ✅ GOOD: `bubble_sort.py`, `HashTable.java`, `factorial.js`

* ❌ BAD: `a.js`, `test_code.py`, `algo.c`

## ✍️ Code Quality & PR Formatting
We have removed strict style rules (indentation, brace placement) to encourage contribution, but we still expect clean, readable code.

1. **Universal Code Quality Rules**
   * **Functionality:** The code must execute without errors and produce the expected result.
   * **Clarity:** Use inline comments where the logic is not immediately obvious.<br>The primary purpose is to teach the pattern.
   * **Minimalism:** Keep the snippet as short and focused as possible.<br>Avoid unnecessary external dependencies.

2. **Pull Request Template**
   Please use this simple template in your PR description.

```
## Snippet Details

**Language:** (e.g., Python, C++, Go)
**Concept Path:** (e.g., Algorithms, DataStructures, OOP)
**File Path:** (e.g., Snippets/Algorithms/Python/quicksort.py)

## Check List

- [ ] The code is placed in the correct `Snippets/[Concept]/[Language]/` folder.
- [ ] The code is functional and well-commented.
- [ ] The PR submission is limited to one single snippet.

```   
4. **Commit Formatting**
   
Please use atomic commits (one commit per feature/snippet) with the following format:

* Format: ```<type>: <description>```

* ✅ GOOD: ```feat(python): Add Binary Search Implementation```

* ❌ BAD: fixed bug, pr 1, new code

## 🚩 Hacktoberfest Success
We want your PRs to count!

* **Avoid Spam:** Contributions must be meaningful and adhere to all code quality standards. Low-effort or trivial PRs will be marked as ```spam``` and will not count.

* **Label Confirmation:** Your PR will be reviewed as quickly as possible. Once accepted, a maintainer will add the ```hacktoberfest-accepted``` label. Only then will it count toward your progress.

**Thank you for your contribution! Happy Hacking! 💻**
