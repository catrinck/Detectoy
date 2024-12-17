import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div className="login-form-wrap">
          <form className="login-form"> 
            <input type = "email" name = "email" placeholder="Email" required/>
            <input type = "password" name = "password" placeholder="Senha" required/>
            <button type = "submit" className="btn-login">Login</button>
            <button type = "submit" className="btn-cadastro">Não tem login? Cadastre-se</button>
          </form>
        </div>
      </header>
    </div>
  );
}

export default App;
