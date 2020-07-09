# LAMBDA-CLOUDWATCH-EC2
Schedule a Cron Job to Run an AWS Lambda Function - Ligar e desligar instância de acordo com o horário programado

Crie uma instância EC2;
Vá no IAM e crie uma Função e Política de acordo com esse JSON de política de acordo com o arquivo "policy-start-stop.json";
Crie a um lambda de start em python e vincule a Role já existente, a que acabou de ser feita;
  Cole a função python "start-instance.py";
Crie a um lambda de stop em python e vincule a Role já existente, a mesma que foi vinculada no de start;
  Cole a função python "stop-instance.py";
Vá até as Rules do CloudWatch:
  Este exemplo da imagem "cloudwatch.png" é o de start para iniciar a EC2 às 07h de segunda à sexta-feira;
  Para fazer o de stop é a mesma maneira, porém vincule o lambda de stop e coloque um cron “00 22 ? * MON-FRI *” para dar stop às 19h;
  Lembrando que há uma diferença de 3h entre Brasil e UTC.
Não há necessidade de criar uma Role para a EC2!

Referência Bibliográfica:
https://www.linkedin.com/pulse/automa%C3%A7%C3%A3o-e-redu%C3%A7%C3%A3o-de-custos-na-aws-utilizando-tags-pierre-rezende/
