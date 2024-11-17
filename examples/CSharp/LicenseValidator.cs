using System;
using System.IO;
using System.Security.Cryptography;
using System.Text;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

public class LicenseValidator
{
    private readonly ILogger _logger;
    private readonly HardwareFingerprint _fingerprint;

    public LicenseValidator()
    {
        _logger = new Logger();
        _fingerprint = new HardwareFingerprint();
    }

    public ValidationResult ValidateLicense(string licenseFile, string licenseKey, bool validateFootprint = true)
    {
        try
        {
            // 加载并解密许可证文件
            string encryptedLicense = File.ReadAllText(licenseFile);
            if (string.IsNullOrEmpty(encryptedLicense))
            {
                return ValidationFailed("无法加载许可证文件");
            }

            string decryptedLicense = Decrypt(encryptedLicense, licenseKey);
            var licenseData = JsonConvert.DeserializeObject<JObject>(decryptedLicense);

            // 生成当前硬件指纹
            string currentHardwareFingerprint = _fingerprint.GenerateFingerprint();
            if (validateFootprint && licenseData["hardware_fingerprint"].ToString() != currentHardwareFingerprint)
            {
                return ValidationFailed("硬件指纹不匹配");
            }

            // 检查许可证是否过期
            long currentTime = DateTimeOffset.UtcNow.ToUnixTimeSeconds();
            long expiresAt = licenseData["expires_at"].ToObject<long>();
            long issuedAt = licenseData["issued_at"].ToObject<long>();

            if (currentTime > expiresAt || currentTime < issuedAt)
            {
                return ValidationFailed("许可证已过期");
            }

            var result = new ValidationResult
            {
                Valid = true,
                Expiry = expiresAt,
                Features = licenseData["features"].ToObject<string[]>(),
                MaxUsers = licenseData["max_users"].ToObject<int>()
            };

            _logger.Info($"许可证验证成功，详情: {JsonConvert.SerializeObject(result)}");
            return result;
        }
        catch (Exception e)
        {
            _logger.Error($"许可证验证错误: {e.Message}");
            return ValidationFailed(e.Message);
        }
    }

    private string Decrypt(string encryptedText, string key)
    {
        // 解密逻辑
        return "dummy_decrypted_license";
    }

    private ValidationResult ValidationFailed(string message)
    {
        return new ValidationResult
        {
            Valid = false,
            Message = message
        };
    }
}

public class ValidationResult
{
    public bool Valid { get; set; }
    public long Expiry { get; set; }
    public string[] Features { get; set; }
    public int MaxUsers { get; set; }
    public string Message { get; set; }
}

public class Logger
{
    public void Info(string message) => Console.WriteLine($"INFO: {message}");
    public void Error(string message) => Console.WriteLine($"ERROR: {message}");
}

public class HardwareFingerprint
{
    public string GenerateFingerprint()
    {
        // 生成硬件指纹的逻辑
        return "dummy_fingerprint";
    }
}