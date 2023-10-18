import Box from '@mui/material/Box';
import './index.css';

const StackRender = () => {
    const techs = [
        { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original-wordmark.svg", alt: "React" },
        { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redux/redux-original.svg", alt: "Redux" },
        { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg", alt: "JavaScript" },
        { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original-wordmark.svg", alt: "CSS" },
        { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/materialui/materialui-original.svg", alt: "Material-UI" },
        { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg", alt: "Python" },
        { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original-wordmark.svg", alt: "SQLalchemy" },
        { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg", alt: "SQLite3 (for development)" },
        { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original-wordmark.svg", alt: "PostgreSQL (for production)" },
        { src: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original.svg", alt: "AWS" }
    ];

    return (
        <Box component="footer" className="footer">
            <div className="tech-section">
                {techs.map((tech, index) => (
                    <img key={index} src={tech.src} alt={tech.alt} className="tech-icon" />
                ))}
            </div>
            <div className="profile-section">
                <div className="personal-links">
                    <a href="https://martynodlrr.site/" target="_blank" rel="noopener noreferrer">Portfolio</a>
                    <a href="https://github.com/Martynodlrr" target="_blank" rel="noopener noreferrer">GitHub</a>
                    <a href="https://www.linkedin.com/in/martynodlrr/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
                </div>
                <img src="https://media.licdn.com/dms/image/D5603AQGPnwv4xdOy_w/profile-displayphoto-shrink_100_100/0/1695828000081?e=1701907200&v=beta&t=f9GwhnCMaOtypzydwv-ByzeXJnmZUgxLq9GIZixbT7A" alt="Your Picture" className="profile-pic" />
            </div>
        </Box>
    );
};

export default StackRender;
