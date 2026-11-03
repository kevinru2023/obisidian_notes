# Tips for Improving Your C++ Code

## Key Concepts to Understand

1. **Case Sensitivity**
   - C++ is case-sensitive
   - Your struct definitions use `Spell`, `Spellbook`, and `Wizard`
   - You must use exactly these names everywhere in your code

2. **References vs Values**
   - When passing large objects (like structs), use references (`&`) to avoid copying
   - Use `const` references when you don't need to modify the object
   - Example: `void displaySpellbook(const Spellbook &book)` instead of `void displaySpellbook(Spellbook book)`

3. **Memory Management**
   - Always match `new` with `delete`
   - Always match `new[]` with `delete[]`
   - Set pointers to `nullptr` after deleting
   - Check if files are open before using them
   - Close files when you're done

4. **Input Validation**
   - Always check if file operations succeeded
   - Validate user input before using it
   - Provide clear error messages

5. **Program Structure**
   - Break down complex operations into smaller functions
   - Use consistent naming conventions
   - Add comments explaining complex logic
   - Initialize variables before using them

## Common Mistakes to Avoid

1. **Memory Leaks**
   - Not deleting allocated memory
   - Not handling all cleanup when errors occur
   - Forgetting to close files

2. **Undefined Behavior**
   - Using uninitialized variables
   - Accessing deleted memory
   - Array out of bounds access

3. **Input/Output Errors**
   - Not checking if file operations succeeded
   - Not clearing input buffer after failed reads
   - Not handling invalid input

4. **Struct Usage**
   - Using incorrect case for struct names
   - Copying large structs instead of using references
   - Not initializing all struct members

## Best Practices

1. **Error Handling**
   ```cpp
   if (!file.is_open()) {
       cerr << "Error: Could not open file" << endl;
       return;
   }
   ```

2. **Memory Management**
   ```cpp
   // Good
   Spell* spells = new Spell[size];
   // ... use spells ...
   delete[] spells;
   spells = nullptr;
   ```

3. **Reference Parameters**
   ```cpp
   // Good
   void updateSpellbook(Spellbook &book)
   
   // Even better when not modifying
   void displaySpellbook(const Spellbook &book)
   ```

4. **File Operations**
   ```cpp
   ifstream file(filename);
   if (!file) {
       cerr << "Error opening file" << endl;
       return;
   }
   // ... use file ...
   file.close();
   ```
