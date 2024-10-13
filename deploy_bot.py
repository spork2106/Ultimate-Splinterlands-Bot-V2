import subprocess
import os
import platform

# Your account details
ACCOUNT_NAME = "acolyte_20684"

# Step 1: Clone the repository
def clone_repo():
    try:
        print("Cloning the repository...")
        subprocess.check_call(["git", "clone", "https://github.com/spork2106/Ultimate-Splinterlands-Bot-V2.git"])
    except subprocess.CalledProcessError:
        print("Error cloning the repository. Please check if Git is installed.")

# Step 2: Install .NET Core if not installed
def install_dotnet():
    try:
        print("Checking .NET installation...")
        subprocess.check_call(["dotnet", "--version"])
        print(".NET is already installed.")
    except subprocess.CalledProcessError:
        print(".NET not found. Installing...")
        if platform.system() == "Windows":
            subprocess.check_call(["dotnet-sdk", "--install"])
        elif platform.system() == "Linux":
            subprocess.check_call(["sudo", "apt", "install", "dotnet-sdk-6.0", "-y"])

# Step 3: Build the bot solution
def build_bot():
    os.chdir("Ultimate-Splinterlands-Bot-V2")
    print("Building the bot...")
    try:
        subprocess.check_call(["dotnet", "restore"])
        subprocess.check_call(["dotnet", "build"])
        print("Build completed successfully.")
    except subprocess.CalledProcessError:
        print("Build failed. Please check for errors.")

# Step 4: Deploy the bot
def deploy_bot():
    print("Deploying the bot for account:", ACCOUNT_NAME)
    try:
        config_path = os.path.join("Config", "config.txt")
        with open(config_path, "w") as config_file:
            config_file.write(f"ACCOUNT_NAME={ACCOUNT_NAME}\n")
            config_file.write("RANKED_FORMAT=wild\n")
            config_file.write("START_BATTLE_ABOVE_ECR=50\n")
            config_file.write("STOP_BATTLE_BELOW_ECR=1\n")
            config_file.write("SHOW_SPS_REWARD=true\n")
            config_file.write("THREADS=1\n")
        print("Configuration file created.")
        subprocess.check_call(["dotnet", "run"])
    except Exception as e:
        print(f"Error during deployment: {e}")

# Step 5: Main function to execute the steps
def main():
    clone_repo()
    install_dotnet()
    build_bot()
    deploy_bot()

if __name__ == "__main__":
    main()
