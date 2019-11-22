defmodule Orwell.MixProject do
  use Mix.Project

  def project do
    [
      app: :orwell,
      version: "0.1.0",
      elixir: "~> 1.7",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  # Run "mix help compile.app" to learn about applications.
  def application do
    [
      extra_applications: [:logger]
    ]
  end

  # Run "mix help deps" to learn about dependencies.
  defp deps do
    [
      {:google_api_storage, "~> 0.0.1"},
      {:goth, "~> 0.6.0"},
      {:google_api_analytics, "~> 0.5"}
    ]
  end
end
