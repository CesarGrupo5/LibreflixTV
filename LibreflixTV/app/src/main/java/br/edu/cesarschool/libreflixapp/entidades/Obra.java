package br.edu.cesarschool.libreflixapp.entidades;

import java.time.LocalDate;

public class Obra {
    private int id;
    private String titulo;
    private String descricacao;
    private LocalDate dataLancamento;
    private String diretor;
    private boolean isPopular;
    private boolean isDestaque;
    private boolean isNovo;
    private Generos[] generos;

    public Obra(int id, String titulo, String descricacao, LocalDate dataLancamento, String diretor, boolean isPopular, boolean isDestaque, boolean isNovo, Generos[] generos) {
        this.id = id;
        this.titulo = titulo;
        this.descricacao = descricacao;
        this.dataLancamento = dataLancamento;
        this.diretor = diretor;
        this.isPopular = isPopular;
        this.isDestaque = isDestaque;
        this.isNovo = isNovo;
        this.generos = generos;
    }

    public int getId() { return id; }

    public String getTitulo() {
        return titulo;
    }

    public String getDescricacao() {
        return descricacao;
    }

    public LocalDate getDataLancamento() {
        return dataLancamento;
    }

    public String getDiretor() {
        return diretor;
    }

    public boolean isPopular() {
        return isPopular;
    }

    public boolean isDestaque() {
        return isDestaque;
    }

    public boolean isNovo() {
        return isNovo;
    }

    public Generos[] getGeneros() {
        return generos;
    }
}
