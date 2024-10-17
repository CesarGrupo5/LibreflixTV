package br.edu.cesarschool.libreflixapp.entidades;

import android.annotation.SuppressLint;

import java.time.LocalDate;

public class Usuario {
    private int id;
    private String nome;
    private String email;
    private String senha;
    private LocalDate dataCadastro;
    private Obra[] obrasFavoritas;
    private Obra[] obrasInteresses;

    @SuppressLint("NewApi")
    public Usuario(int id, String nome, String email, String senha, String dataCadastro) {
        this.id = id;
        this.nome = nome;
        this.email = email;
        this.senha = senha;
        this.dataCadastro = LocalDate.parse(dataCadastro);
    }

    public Usuario(String username, String email, String senha) {
    }

    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public String getSenha() {
        return senha;
    }

    public LocalDate getDataCadastro() {
        return dataCadastro;
    }

    public Obra[] getFavoritas() {
        return obrasFavoritas;
    }

    public Obra[] getInteresses() {
        return obrasInteresses;
    }
}
