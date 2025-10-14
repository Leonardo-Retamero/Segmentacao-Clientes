import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title='Segmentação do Cliente',
    page_icon='📊',
    layout='wide'
)

df = pd.read_csv('segmentos.csv')

st.title('Dashboard de Segmentação do Cliente para a Área de Marketing')

bins = [18, 25, 30, 35, 40, 50, 60, 70]
labels = ['18-25', '26-30', '31-35', '36-40', '41-50', '51-60', '61-70']

df['faixa_idade'] = pd.cut(df['idade'], bins=bins, labels=labels, right=True)

if not df.empty:
    media_pontuacao = df['pontuacao_gastos'].mean()
    media_idade = df['idade'].mean()
    media_renda = df['renda_anual'].mean()
    total_clientes = df['id'].count()
else:
    media_pontuacao, media_idade, media_renda, total_clientes = 0, 0, 0, 0

col1, col2, col3, col4 = st.columns(4)
col1.metric('Média de Pontuação de Gastos', f'{media_pontuacao:,.2f}')
col2.metric('Média de Idade', f'{media_idade:,.0f}')
col3.metric('Média de Renda Anual', f'{media_renda:,.2f}')
col4.metric('Total de Clientes', total_clientes)

st.markdown('---')

col_graf1 = st.columns(1)

with col_graf1[0]:
    if not df.empty:
        distribuicao_salario = df.groupby('faixa_idade', as_index=False).agg(
            {'renda_anual': 'mean',
             'idade': 'count'}).rename(columns={'idade': 'quantidade'}).sort_values('faixa_idade')
        grafico_barra = px.bar(
            distribuicao_salario,
            x='faixa_idade',
            y='renda_anual',
            text='quantidade',
            title='Distribuição da Renda Média Anual por Faixa de Idade',
            labels={'faixa_idade': 'Faixa de Idade', 
                    'renda_anual': 'Renda Anual',
                    'quantidade': 'Quantidade de Pessoas'
            },
            color_discrete_sequence=['#005b8a']
        )
        grafico_barra.update_traces(textposition='outside')
        st.plotly_chart(grafico_barra, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir")

col_graf2, col_graf3 = st.columns(2)

with col_graf2:
    if not df.empty:
        top_gastos = df.groupby('cluster')['pontuacao_gastos'].mean().sort_values(ascending=True).reset_index()
        top_gastos['cluster'] = top_gastos['cluster'].astype(str)
        cores = ['#007bad', '#005b8a', '#003b67']
        top_gastos['cor'] = cores[:len(top_gastos)]
        fig_bar1 = px.bar(
            top_gastos,
            x='pontuacao_gastos',
            y='cluster',
            orientation='h',
            title='Média de Pontuação de Gastos por Segmento',
            labels={'cluster': 'Segmento',
                    'pontuacao_gastos': 'Pontuação Gastos'},
            text='pontuacao_gastos',
            color='cor',
            color_discrete_map='identity'
        )
        fig_bar1.update_yaxes(type='category')
        fig_bar1.update_traces(
            textposition='outside',
            texttemplate='%{x:.0f}',
            textfont=dict(color='white')
        )
        st.plotly_chart(fig_bar1, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir')

with col_graf3:
    if not df.empty:
        renda_anual = df.groupby('cluster')['renda_anual'].mean().sort_values(ascending=True).reset_index()
        renda_anual['cluster'] = renda_anual['cluster'].astype(str)
        cores = ['#007bad', '#005b8a', '#003b67']
        renda_anual['cor'] = cores[:len(renda_anual)]
        fig_bar2 = px.bar(
            renda_anual,
            y='cluster',
            x='renda_anual',
            orientation='h',
            title='Média de Renda Anual por Segmento',
            labels={'cluster': 'Segmento',
                    'renda_anual': 'Renda Média'},
            text='renda_anual',
            color='cor',
            color_discrete_map='identity', 
        )
        fig_bar2.update_yaxes(type='category')
        fig_bar2.update_traces(
            textposition='outside',
            texttemplate='%{x:.0f}',
            textfont=dict(color='white')
        )
        st.plotly_chart(fig_bar2, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir')

col_graf4, col_graf5 = st.columns(2)

with col_graf4:
    if not df.empty:
        fig_bar3 = go.Figure(go.Waterfall(
            orientation='v',
            measure=['relative', 'relative', 'relative', 'total'],
            x=['1', '2', '0', 'Total'],
            textposition='inside',
            textfont=dict(color='white'),
            text=['187', '167', '146', '500'],
            y=[187, 167, 146, 0],
            connector={'line': {'color': 'rgb(63, 63, 63)'}},
            increasing=dict(marker=dict(color='#5885d9')),
            decreasing=dict(marker=dict(color='#5885d9')),
            totals=dict(marker=dict(color='#2e62b2'))
        ))
        fig_bar3.update_xaxes(type='category')
        fig_bar3.update_layout(
            title='Total de Clientes por Segmento',
            showlegend=True
        )
        st.plotly_chart(fig_bar3, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir')

color1 = ['#2b6cb3', '#568fd9', '#80b2ff']

with col_graf5:
    if not df.empty:
        idade_segmento = df.groupby('cluster')['idade'].mean().reset_index()
        idade_segmento['idade'] = idade_segmento['idade'].round(0).astype(int)
        fig_bar4 = px.pie(
            idade_segmento,
            values='idade',
            names='cluster',
            color_discrete_sequence=color1,
            title='Média de Idade por Segmento',
            hole=0.5
        )                     
        fig_bar4.update_traces(
            textinfo='percent+value',
            textfont=dict(size=14, color='white'),
            showlegend=True
        )
        fig_bar4.update_layout(
            legend_title_text='Segmentos'
        )
        
        st.plotly_chart(fig_bar4, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir')