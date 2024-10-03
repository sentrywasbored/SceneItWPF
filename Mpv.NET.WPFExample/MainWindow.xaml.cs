using System;
using System.Diagnostics;
using System.Security.Cryptography.X509Certificates;
using System.Windows;
using System.Windows.Input;
using System.IO;
using Mpv.NET.Player;
using System.Security.Policy;
using System.Windows.Threading;
using System.Linq.Expressions;

namespace Mpv.NET.WPFExample
{
	public partial class MainWindow : Window
	{
		private DispatcherTimer _timer;
		private MpvPlayer player1;
		private MpvPlayer player2;
		private MpvPlayer currentPlayer;
		private MpvPlayer nextPlayer;
		private string gameVer;
		string url;
		string newfile;
		string _file;
		

        public MainWindow()
		{
            
            InitializeComponent();
			_timer = new DispatcherTimer();
			_timer.Interval = TimeSpan.FromMilliseconds(16);
			_timer.Tick += OnUpdate;
			_timer.Start();
			PlayerHost.BackColor = System.Drawing.Color.Black;
			gameVer = "Bond_Special";
			_file = "ToGameMenu";
			player1 = CreatePlayer();
			player2 = CreatePlayer();

			currentPlayer = player1;
			nextPlayer = player2;
			url = updateUrl(_file);
			Debug.WriteLine(url);
			LoadVideo(_file, currentPlayer);
			currentPlayer.Resume();
		}

		private MpvPlayer CreatePlayer()
		{
			var player = new MpvPlayer(PlayerHost.Handle)
			{
				Loop = false,
				Volume = 50
			};
			player.MediaFinished += NextVid;
			return player;
		}

		string updateUrl (string filename)
		{
            string output = Path.Combine(Directory.GetCurrentDirectory(), "Resources", gameVer, filename + ".mkv");
            return output;

        }

        string updateUrl(string filename, string gameMode)
        {
			string output;
			if (gameMode == "AllPlay")
			{
                Random r = new Random();
                int rInt = r.Next(0, 262);
				string random = rInt.ToString();
                output = Path.Combine(Directory.GetCurrentDirectory(), "Resources", gameVer, gameMode, gameMode + random + ".mkv");
			}
			else if (gameMode == "MyPlay")
			{
                Random r = new Random();
                int rInt = r.Next(0, 262);
                string random = rInt.ToString();
                output = Path.Combine(Directory.GetCurrentDirectory(), "Resources", gameVer, gameMode, gameMode + random, "Prompt.mkv");
			}
			else
			{
                output = Path.Combine(Directory.GetCurrentDirectory(), "Resources", gameVer, filename + ".mkv");
            }
            return output;

        }

        private void OnUpdate(object sender, EventArgs e)
		{
			
			
			if (_file == "OptreveLogo")
			{
				newfile = "ScreenlifeLogo";
			}
			if (_file == "ScreenlifeLogo")
			{
				newfile = "MainMenuFirstTime";
			}
			if (_file == "MainMenuFirstTime")
			{
				newfile = "MainMenu";
			}
			if (_file == "MainMenu")
			{
				newfile = "MainMenu";
			}
            if (_file == "GameMenu")
            {
                newfile = "GameMenu";
            }
            if (_file == "ToGameMenu")
            {
                newfile = "GameMenu";
            }
            if (_file.StartsWith("AllPlay"))
			{
				newfile = "GameMenu";
			}
			if (_file.StartsWith("Question"))
			{
				newfile = "GameMenu";
			}

            if (newfile != null)
            {
                LoadVideo(newfile, nextPlayer);
            }

        }
        private void NextVid(object sender, EventArgs e)
        {
            Debug.WriteLine("NextVid Ran");
            _file = newfile;
            Debug.WriteLine(_file);
            Debug.WriteLine(updateUrl(_file));

            // Switch players
            var temp = currentPlayer;
            currentPlayer = nextPlayer;
            nextPlayer = temp;

            // Hide the previous player and show the current one
            nextPlayer.API.SetPropertyString("video-sync", "audio");
            currentPlayer.API.SetPropertyString("video-sync", "display-resample");

            currentPlayer.Resume();
        }

        private void LoadVideo(string file, MpvPlayer player)
        {
            url = updateUrl(file);
            Debug.WriteLine($"Loading {url} into {(player == player1 ? "player1" : "player2")}");
            player.Load(url);
            player.Pause(); // Pause immediately after loading
        }
        private void WindowOnClosing(object sender, System.ComponentModel.CancelEventArgs e)
		{
			nextPlayer.Dispose();
			currentPlayer.Dispose();
		}
	}
}