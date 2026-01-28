# Entry point for uvx command
from main import *

if __name__ == "__main__":
    import sys
    print("Starting gNucleus MCP Server...", file=sys.stderr)
    
    # Load environment variables
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    GNUCLEUS_HOST = os.getenv("GNUCLEUS_HOST")
    GNUCLEUS_API_KEY = os.getenv("GNUCLEUS_API_KEY")
    GNUCLEUS_ORG_ID = os.getenv("GNUCLEUS_ORG_ID")
    
    print(f"GNUCLEUS_HOST is {GNUCLEUS_HOST}", file=sys.stderr)
    if GNUCLEUS_ORG_ID:
        print(f"GNUCLEUS_ORG_ID is {GNUCLEUS_ORG_ID}", file=sys.stderr)
    
    # Initialize and run the server
    try:
        mcp.run(transport='stdio')
    except Exception as e:
        print(f"Server error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)