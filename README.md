# Basic Setup


Follow these steps to set up the project:

1. **Install `uv`**
    - Make sure you have `uv` installed on your system.

2. **Create Project Folder**
    - Create a folder named `fastmcp-demo-server`.

3. **Open in VS Code**
    - Open the `fastmcp-demo-server` folder in Visual Studio Code.

4. **Initialize the Project**
    - Open the terminal in VS Code.
    - Run:
      ```sh
      uv init
      ```

5. **Add FastMCP Dependency**
    - Run:
      ```sh
      uv add fastmcp
      ```

6. **Check FastMCP Version**
    - (Optional) Verify the installed version of FastMCP.

7. **Create a Basic Server**
    - Create a `main.py` file with your server code.

8. **Test the Server**
    - Run the development server:
      ```sh
      uv run fastmcp dev main.py
      ```

9. **Run the Server**
    - Start the server normally:
      ```sh
      uv run fastmcp run main.py
      ```

10. **Add the Server to Claude Desktop**
     - Install the server for Claude Desktop and run:
        ```sh
        uv run fastmcp install claude-desktop main.py
        ```
     
---

**Note:** Replace `main.py` with your actual server file if different.
