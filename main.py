import random 
from fastmcp import FastMCP


#Create the fastmcp instatnce
mcp = FastMCP(name="Demo Server")


@mcp.tool
def roll_dice(n_dice:int=1)->list[int]:
    """Roll n 6-sided dice and return the results as a list of integers."""
    return [random.randint(1, 6) for _ in range(n_dice)]


@mcp.tool
def add(a:int,b:int)->int:
    """Add two integers and return the result."""
    return a + b

@mcp.tool
def sub(a:int,b:int)->int:
    """subtract two integers and return the result."""
    return a - b



if __name__ == "__main__":
    mcp.run()